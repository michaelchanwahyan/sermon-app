from datetime import datetime
import pickle as pkl
import numpy as np

'''### define SYMNMF'''
def symnmf( V , opt ) :
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
#                                                                                 #
# Core Reference :                                                                #
# Z. He, S. Xie, R. Zdunek, G. Zhou and A. Cichocki,                              #
# "Symmetric Nonnegative Matrix Factorization: Algorithms and Applications to     #
# Probabilistic Clustering," in IEEE Transactions on Neural Networks, vol. 22,    #
# no. 12, pp. 2117-2131, Dec. 2011.                                               #
# IEEE Explore Link :                                                             #
# http://ieeexplore.ieee.org/document/6061964/                                    #
#                                                                                 #
# Symmetric Nonnegative Matrix Factorization (SymNMF) is to solve the followg     #
# problem where V \in \R_+^{NxN} is given : Find a P \in \R_+^{NxK} solving       #
#                                                                                 #
#    ---------------------------------                                            #
#   |    min   || V - P*P^t ||_F^2    |  (Problem 1)                              #
#   |    s.t.  P >= 0                 |                                           #
#    ---------------------------------                                            #
#                                                                                 #
#    ---------------------------------                                            #
#   |    min   || V - P*Q   ||_F^2    |  (Formulation 2.1)                        #
#   |    s.t.  P >= 0; Q >= 0; P=Q^t  |                                           #
#    ---------------------------------                                            #
#    ~                                                                            #
#    ---------------------------------                                            #
#   |    min   || V - P*Q   ||_F^2    |  (Formulation 2.2)                        #
#   |    s.t.  P >= 0; Q >= 0;        |                                           #
#   |          || P-Q^t || < epsilon  |                                           #
#    ---------------------------------                                            #
#   <=>                                                                           #
#    --------------------------------------------------------                     #
#   |    min   || V - P*Q ||_F^2 + lambda || P - Q^t ||_F^2  | (Problem 2)        #
#   |    s.t.  P >= 0; Q >= 0                                |                    #
#    --------------------------------------------------------                     #
#                                                                                 #
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
#                                                                                 #
#   a similar problem in doing symmetric NMF : with PSD sandwiched                #
#   it is very likely to be applied in Sym-NMF a matrix of format Z = Y^t*T       #
#   where Y lives inside an NMF model Y = A*S.                                    #
#                                                                                 #
#   YtY = Y^T * Y = S^T * A^T * A * S = St * AtA * S                              #
#                                                                                 #
#    ---------------------------------                                            #
#   |    min   || V - P*W*P^T ||_F^2  |  (Problem 3)                              #
#   |    s.t.  P >= 0 , W \in PSD     |                                           #
#    ---------------------------------                                            #
#                                                                                 #
#   this problem cannot be solved by multiplicative update type method            #
#   i.e. BLAS-MU type is not applicable. we can only use gradient type methods    #
#                                                                                 #
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
#                                                                                 #
# Input:                                                                          #
#     V           : input nonnegative matrix of square shape                      #
# opt:K           : rank                                                          #
# opt:P0          : initial guess on the estimate                                 #
# opt:method      : method used for the symmetric NMF                             #
#                   it could be 'LV3-BLAS-PARALLEL-MU'          ; solve Prob 1    #
#                               'BETA-BLAS-PARALLEL-MU'         ; solve Prob 1    #
#                               'ExBCD-GRAD-UPDATE'             ; solve Prob 2    #
#                               'InExBCD-GRAD-UPDATE'           ; solve Prob 2    #
#                               'ExBCD-GRAD-UPDATE-PSD'         ; solve Prob 3    #
#                               'InExBCD-GRAD-UPDATE-PSD'       ; solve Prob 3    #
# opt:maxIteraNum    : max iteration number, default is 1e6                       #
# opt:convThresh     : objective value convergence threshold, default is 1e-4     #
# opt:beta           : beta value in BETA-BLAS-PARALLEL-MU, default is 0.99       #
#                      > required when using BETA-BLAS-PARALLEL-MU                #
# opt:lambdaVal      : lambda value in GRAD type methods, default is 1000         #
#                      > required when using ExBCD-GRAD-UPDATE                    #
#                                            InExBCD-GRAD-UPDATE                  #
#                                            ExBCD-GRAD-UPDATE-MTRXCOMPL          #
#                                            InExBCD-GRAD-UPDATE-MTRXCOMPL        #
# opt:subMaxIteraNum : max iteration number in subproblems, default is 1e3        #
# opt:subConvThresh  : conv. threshold in subproblems, default is 1e-3            #
# opt:grdMthdType    : gradient method type, default use proximal gradient method #
#                                                                                 #
# This function mainly implements the following 2 SymNMF algorithms, they are     #
# - Basic Level-3 BLAS Parallel Multiplicative Update (17)                        #
# - Fast Parallel beta-SymNMF Algorithm (Algorithm 4) with default beta = 0.99    #
#                                                                                 #
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
    # ========================
    # Get Dimension of input V
    # ========================
    N1 , N2 = V.shape
    if( N1 != N2 ) :
        print( "ERROR @ NMF.SYMNMF(): input matrix is non-square !!!" )
        return 0
    else :
        N = N1

    # ======================
    # Check Input Parameters
    # ======================
    # general settings required by any method
    K              = opt['K'             ] if 'K'              in opt else 5
    P0             = opt['P0'            ] if 'P0'             in opt else np.random.rand( N , K )
    if 'Q0' in opt :
        Q0         = opt['Q0'            ]
    W_PSD_0        = opt['W_PSD'         ] if 'W_PSD'          in opt else np.identity( K )
    method         = opt['method'        ] if 'method'         in opt else 'LV3-BLAS-PARELLEL-MU'
    maxIteraNum    = opt['maxIteraNum'   ] if 'maxIteraNum'    in opt else int(1e6)
    convThresh     = opt['convThresh'    ] if 'convThresh'     in opt else 1e-4
    verboseIntvl   = opt['verboseIntvl'  ] if 'verboseIntvl'   in opt else 100
    # settings required by beta BLAS parallel MU
    beta           = opt['beta'          ] if 'beta'           in opt else 0.99
    # settings required by gradient type AO (BCD)
    lambdaVal      = opt['lambdaVal'     ] if 'lambdaVal'      in opt else 1
    subMaxIteraNum = opt['subMaxIteraNum'] if 'subMaxIteraNum' in opt else 1000
    subConvThresh  = opt['subConvThresh' ] if 'subConvThresh'  in opt else 1e-3
    grdMthdType    = opt['grdMthdType'   ] if 'grdMthdType'    in opt else 'prox'

    # ==================
    # Get Initialization
    # ==================
    P_curr = np.copy( P0 )
    objVal = []
    objVal.append( symnmf_froNormSquare( V , P_curr ) )
    if method == 'LV3-BLAS-PARALLEL-MU' :
        # ===========================================
        # Level-3 BLAS Parallel MU (update rule (17))
        # ===========================================
        for k in range( 0 , maxIteraNum ) :
            numera = V.dot( P_curr )
            denomi = P_curr.dot( P_curr.T.dot( P_curr ) )
            P_curr = np.multiply( P_curr , np.cbrt( np.divide( numera , denomi + 0.00000001 ) ) )
            objVal.append( symnmf_froNormSquare( V , P_curr ) )
            objChng = abs( objVal[k+1] - objVal[k] ) / objVal[k+1]
            if( k % verboseIntvl == 0 ) :
                print( str(datetime.datetime.now()) + "it : %d objChng : %1.6e objVal : %1.6e" % ( k , objChng , objVal[k+1] ) )
            if objChng < convThresh or objVal[k+1] < 1e-6 :
                return P_curr , objVal
                break
            if os.path.exists( "stop.txt" ) :
                os.system( "rm -f stop.txt" )
                return P_curr , objVal
                break
        return P_curr , objVal
    elif method == 'BETA-BLAS-PARALLEL-MU' :
        # ========================================
        # Level-3 BLAS Parallel MU (Algorithm (4))
        # ========================================
        for k in range( 0 , maxIteraNum ) :
            numera = V.dot( P_curr )
            denomi = P_curr.dot( P_curr.T.dot( P_curr ) )
            R      = np.divide( numera , denomi + 0.00000001 )
            P_curr = np.multiply( P_curr , 1 - beta + beta * R )
            objVal.append( symnmf_froNormSquare( V , P_curr ) )
            if objVal[k+1] >= objVal[k] :
                if( k % verboseIntvl == 0 ) :
                    print( "prevObj : %f" % objVal[k  ] )
                    print( "currObj : %f" % objVal[k+1] )
                P_curr = np.divide( P_curr , 1 - beta + beta * R )
                P_curr = np.multiply( P_curr , np.cbrt( R ) )
                objVal[k+1] = symnmf_froNormSquare( V , P_curr )
                if( k % verboseIntvl == 0 ) :
                    print( "beta - SNNMF renewObj : %f" % objVal[k+1] )
            objChng = abs( objVal[k+1] - objVal[k] ) / objVal[k+1]
            if( k % verboseIntvl == 0 ) :
                print( str(datetime.datetime.now()) + "it : %d objChng : %1.6e objVal : %1.6e" % ( k , objChng , objVal[k+1] ) )
            if objChng < convThresh or objVal[k+1] < 1e-6  :
                return P_curr , objVal
                break
            if os.path.exists( "stop.txt" ) :
                os.system( "rm -f stop.txt" )
                return P_curr , objVal
                break
        return P_curr , objVal
    elif method == 'ExBCD-GRAD-UPDATE' :
        # ====================================
        # we are solving the following problem
        #  -------------------------------------
        # | min  || V-PQ || + lambda || P-Qt || |
        # | s.t. P >= 0 ; Q >= 0                |
        #  -------------------------------------
        # by alternating optimization (AO)
        # aka (Block Coordinate Descent BCD)
        # ====================================
        if "Q0" in locals() :
            print( "obtain Q0 as Q init !" )
            Q_curr = Q0
        else :
            Q_curr = np.copy( P_curr.T )
        for k in range( 0 , maxIteraNum ) :
            Q_curr    = symnmf_gradUpd( V   , P_curr   , Q_curr   , lambdaVal , subMaxIteraNum , subConvThresh , grdMthdType )
            P_curr_Tr = symnmf_gradUpd( V.T , Q_curr.T , P_curr.T , lambdaVal , subMaxIteraNum , subConvThresh , grdMthdType )
            P_curr    = P_curr_Tr.T
            objVal.append( symnmf_froNormSquare( V , P_curr , Q_curr , lambdaVal ) )
            objChng = abs( objVal[k+1] - objVal[k] ) / objVal[k+1]
            if( k % verboseIntvl == 0 ) :
                print( str(datetime.datetime.now()) + "it : %d objChng : %1.6e objVal : %1.6e" % ( k , objChng , objVal[k+1] ) )
            if objChng < convThresh or objVal[k+1] < 1e-6  :
                print( "average error between P and Qt : %f" % np.divide( np.sum(np.abs(P_curr-Q_curr.T)) , P_curr.size ) )
                return P_curr , Q_curr , objVal
                break
            if os.path.exists( "stop.txt" ) :
                os.system( "rm -f stop.txt" )
                print( "average error between P and Qt : %f" % np.divide( np.sum(np.abs(P_curr-Q_curr.T)) , P_curr.size ) )
                return P_curr , Q_curr , objVal
                break
        print( "average error between P and Qt : %f" % np.divide( np.sum(np.abs(P_curr-Q_curr.T)) , P_curr.size ) )
        return P_curr , Q_curr , objVal
    elif method == 'InExBCD-GRAD-UPDATE' :
        # ====================================
        # we are solving the following problem
        #  -------------------------------------
        # | min  || V-PQ || + lambda || P-Qt || |
        # | s.t. P >= 0 ; Q >= 0                |
        #  -------------------------------------
        # by alternating optimization (AO)
        # aka (Block Coordinate Descent BCD)
        # ====================================
        if "Q0" in locals() :
            print( "obtain Q0 as Q init !" )
            Q_curr = Q0
        else :
            Q_curr = np.copy( P_curr.T )
        for k in range( 0 , maxIteraNum ) :
            Q_curr    = symnmf_gradUpd( V   , P_curr   , Q_curr   , lambdaVal , subMaxIteraNum , subConvThresh , grdMthdType )
            P_curr_Tr = symnmf_gradUpd( V.T , Q_curr.T , P_curr.T , lambdaVal , subMaxIteraNum , subConvThresh , grdMthdType )
            P_curr    = P_curr_Tr.T
            objVal.append( symnmf_froNormSquare( V , P_curr , Q_curr , lambdaVal ) )
            objChng = abs( objVal[k+1] - objVal[k] ) / objVal[k+1]
            if( k % verboseIntvl == 0 ) :
                print( str(datetime.datetime.now()) + "it : %d objChng : %1.6e objVal : %1.6e" % ( k , objChng , objVal[k+1] ) )
            if objChng < convThresh or objVal[k+1] < 1e-6  :
                print( "average error between P and Qt : %f" % np.divide( np.sum(np.abs(P_curr-Q_curr.T)) , P_curr.size ) )
                return P_curr , Q_curr , objVal
                break
            if os.path.exists( "stop.txt" ) :
                os.system( "rm -f stop.txt" )
                print( "average error between P and Qt : %f" % np.divide( np.sum(np.abs(P_curr-Q_curr.T)) , P_curr.size ) )
                return P_curr , Q_curr , objVal
                break
        print( "average error between P and Qt : %f" % np.divide( np.sum(np.abs(P_curr-Q_curr.T)) , P_curr.size ) )
        return P_curr , Q_curr , objVal
    elif method == 'ExBCD-GRAD-UPDATE-PSD' :
        # ======================================================
        # we are solving the following problem
        #    --------------------------------------------------
        #   |    min   || V - P*W*Q ||_F^2 + lambda || P-Qt || |
        #   |    s.t.  P >= 0 , Q >= 0 , W \in PSD             |
        #    --------------------------------------------------
        # by alternating optimizatino (AO)
        # aka (Block Coordinate Descent BCD)
        # ======================================================
        if "Q0" in locals() :
            print( "obtain Q0 as Q init !" )
            Q_curr = Q0
        else :
            Q_curr = np.copy( P_curr.T )
        if "W_PSD_0" in locals() :
            W_PSD_curr = W_PSD_0
        else :
            print( "W_PSD_0 not in locals() !!! no initial PSD W given !!!" )
        for k in range( 0 , maxIteraNum ) :
            Q_curr     = symnmf_gradUpd( V   , P_curr.dot(W_PSD_curr)   , Q_curr   , lambdaVal , subMaxIteraNum , subConvThresh , grdMthdType )
            P_curr_Tr  = symnmf_gradUpd( V.T , Q_curr.T.dot(W_PSD_curr) , P_curr.T , lambdaVal , subMaxIteraNum , subConvThresh , grdMthdType )
            P_curr     = P_curr_Tr.T
            W_PSD_curr = symnmf_PSDgradUpd( V , P_curr , Q_curr , W_PSD_curr , lambdaVal , subMaxIteraNum , subConvThresh , grdMthdType )
            objVal.append( symnmf_froNormSquare( V , P_curr.dot( W_PSD_curr ) , Q_curr , lambdaVal ) )
            objChng = abs( objVal[k+1] - objVal[k] ) / objVal[k+1]
            if( k % verboseIntvl == 0 ) :
                print( str(datetime.datetime.now()) + "it : %d objChng : %1.6e objVal : %1.6e" % ( k , objChng , objVal[k+1] ) )
            if objChng < convThresh or objVal[k+1] < 1e-6  :
                print( "average error between P and Qt : %f" % np.divide( np.sum(np.abs(P_curr-Q_curr.T)) , P_curr.size ) )
                return P_curr , W_PSD_curr , Q_curr , objVal
                break
            if os.path.exists( "stop.txt" ) :
                os.system( "rm -f stop.txt" )
                print( "average error between P and Qt : %f" % np.divide( np.sum(np.abs(P_curr-Q_curr.T)) , P_curr.size ) )
                return P_curr , W_PSD_curr , Q_curr , objVal
                break
        print( "average error between P and Qt : %f" % np.divide( np.sum(np.abs(P_curr-Q_curr.T)) , P_curr.size ) )
        return P_curr , W_PSD_curr , Q_curr , objVal
    elif method == 'InExBCD-GRAD-UPDATE-PSD' :
        # ======================================================
        # we are solving the following problem
        #    --------------------------------------------------
        #   |    min   || V - P*W*Q ||_F^2 + lambda || P-Qt || |
        #   |    s.t.  P >= 0 , Q >= 0 , W \in PSD             |
        #    --------------------------------------------------
        # by alternating optimizatino (AO)
        # aka (Block Coordinate Descent BCD)
        # ======================================================
        if "Q0" in locals() :
            print( "obtain Q0 as Q init !" )
            Q_curr = Q0
        else :
            Q_curr = np.copy( P_curr.T )
        if "W_PSD_0" in locals() :
            W_PSD_curr = W_PSD_0
        else :
            print( "W_PSD_0 not in locals() !!! no initial PSD W given !!!" )
        for k in range( 0 , maxIteraNum ) :
            Q_curr     = symnmf_gradUpd( V   , P_curr.dot(W_PSD_curr)   , Q_curr   , lambdaVal , subMaxIteraNum , subConvThresh , grdMthdType )
            P_curr_Tr  = symnmf_gradUpd( V.T , Q_curr.T.dot(W_PSD_curr) , P_curr.T , lambdaVal , subMaxIteraNum , subConvThresh , grdMthdType )
            P_curr     = P_curr_Tr.T
            W_PSD_curr = symnmf_PSDgradUpd( V , P_curr , Q_curr , W_PSD_curr , lambdaVal , subMaxIteraNum , subConvThresh , grdMthdType )
            objVal.append( symnmf_froNormSquare( V , P_curr.dot( W_PSD_curr ) , Q_curr , lambdaVal ) )
            objChng = abs( objVal[k+1] - objVal[k] ) / objVal[k+1]
            if( k % verboseIntvl == 0 ) :
                print( str(datetime.datetime.now()) + "it : %d objChng : %1.6e objVal : %1.6e" % ( k , objChng , objVal[k+1] ) )
            if objChng < convThresh or objVal[k+1] < 1e-6  :
                print( "average error between P and Qt : %f" % np.divide( np.sum(np.abs(P_curr-Q_curr.T)) , P_curr.size ) )
                return P_curr , W_PSD_curr , Q_curr , objVal
                break
            if os.path.exists( "stop.txt" ) :
                os.system( "rm -f stop.txt" )
                print( "average error between P and Qt : %f" % np.divide( np.sum(np.abs(np.random.rand(10,2)-np.random.rand(2,10).T)) , np.random.rand(10,2).size ) )
                return P_curr , W_PSD_curr , Q_curr , objVal
                break
        print( "average error between P and Qt : %f" % np.divide( np.sum(np.abs(np.random.rand(10,2)-np.random.rand(2,10).T)) , np.random.rand(10,2).size ) )
        return P_curr , W_PSD_curr , Q_curr , objVal

def symnmf_gradUpd( V , P , Q , lambdaVal , maxIteraNum , convThresh , grdMthdType="prox" ) :
    # solves a subproblem of the whole
    # symnmf problem. subproblem is stated as
    #  -------------------------------------------------
    # | min  || V - PQ ||_F^2 + lambda || P - Qt ||_F^2 |
    # | s.t. Q >= 0                                     |
    #  -------------------------------------------------
    obj_prev = symnmf_froNormSquare( V , P , Q , lambdaVal )
    PtP      = P.T.dot( P )
    eL , _   = np.linalg.eig( PtP )
    max_eL   = 2*np.max( eL.real )
    PtV      = V.dot(P).T
    if grdMthdType == "prox" :
        stepSize = 1/max_eL
        for k in range( maxIteraNum ) :
            GRAD_Q   = 2 * ( ( PtP.dot( Q ) - PtV ) + lambdaVal * (Q - P.T) )
            Q        = np.maximum( Q - stepSize * GRAD_Q , 0 )
            obj_curr = symnmf_froNormSquare( V , P , Q , lambdaVal )
            objChng = abs( obj_curr - obj_prev ) / obj_curr
            if( objChng < convThresh ) :
                    return Q
                    break
            else :
                obj_prev = obj_curr
        return Q
    return Q

def symnmf_PSDgradUpd( V , P , Q , W , lambdaVal , maxIteraNum , convThresh , grdMthdType="prox" ) :
    # solves a subproblem of the whole
    # symnmf problem. subproblem is stated as
    #  ------------------------
    # | min  || V - PWQ ||_F^2 |
    # | s.t. W \in PSD         |
    #  ------------------------
    obj_prev = symnmf_froNormSquare( V , P.dot(W) , Q , lambdaVal )
    PtP      = P.T.dot( P )
    QQt      = Q.dot( Q.T )
    eL , _   = np.linalg.eig( np.kron( PtP , QQt ) )
    max_eL   = 2*np.max( eL.real )
    PtVQt    = P.T.dot( V.dot( Q.T ) )
    if grdMthdType == "prox" :
        stepSize = 1/max_eL
        for k in range( maxIteraNum ) :
            GRAD_W   = 2 * ( PtP.dot( W ).dot( QQt ) - PtVQt )
            W        = W - stepSize * GRAD_W
            # projection onto PSD set
            eL , eV  = np.linalg.eig( W )
            eL       = np.diag( np.maximum( eL.real , 1e-12 ) )
            eV       = eV.real
            W        = eV.dot( eL ).dot( eV.T )
            obj_curr = symnmf_froNormSquare( V , P.dot(W) , Q , lambdaVal )
            objChng = abs( obj_curr - obj_prev ) / obj_curr
            if( objChng < convThresh ) :
                    return W
                    break
            else :
                obj_prev = obj_curr
        return W
    return W

def symnmf_froNormSquare( V , P , Q=None , lambdaVal=0 ) :
    if Q is None :
        return np.sum( np.square( V - P.dot( P.T ) ) )
    else :
        return          np.sum( np.square( V - P.dot( Q ) ) ) + \
               lambdaVal * np.sum( np.square( P.T - Q     ) )

if __name__ == '__main__':
    __main__filename = 'nmf_06_closesermon_symnmf()'

    s2s_cooccur_fname = 'var_05_MAT_S2S_COOCCUR.pkl'
    print(f'[{str(datetime.now())} @ {__main__filename}]    loading {s2s_cooccur_fname} ...')
    with open(s2s_cooccur_fname, 'rb') as fp:
        C = pkl.load(fp)
    fp.close()
    print(f'[{str(datetime.now())} @ {__main__filename}]    done loading {s2s_cooccur_fname} !')

    MO = 20 # model order
    print(f'[{str(datetime.now())} @ {__main__filename}]    model order MO = {MO}')
    opt_symnmf = {}
    opt_symnmf[ 'K'             ] = MO
    opt_symnmf[ 'P0'            ] = np.random.rand( C.shape[0] , MO )
    opt_symnmf[ 'method'        ] = 'BETA-BLAS-PARALLEL-MU'
    opt_symnmf[ 'maxIteraNum'   ] = int(1e4)
    opt_symnmf[ 'convThresh'    ] = 1e-6
    opt_symnmf[ 'beta'          ] = 0.99
    opt_symnmf[ 'verboseIntvl'  ] = int(5e2)
    P , objVal = symnmf( C , opt_symnmf )
    P[ P < 1e-12 ] = 0
    print(f'[{str(datetime.now())} @ {__main__filename}]    saving sym-nmf results ...')
    np.savetxt( 'var_06_P.txt' , P , fmt='%1.8e' )
    print(f'[{str(datetime.now())} @ {__main__filename}]    done saving sym-nmf results !')
