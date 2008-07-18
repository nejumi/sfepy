##
# c: 01.02.2008, r: 26.03.2008

#fileName_mesh = 'database/simple.mesh'
#fileName_mesh = 'database/phono/cube_sphere.mesh'
#fileName_mesh = 'database/t.1.node'
file_name_mesh = 'tmp/t.1.node'

options = {
    'save_eig_vectors' : None,
    'squared' : False,
    'n_eigs' : 13,
    'eigen_solver' : 'eigen1',
}

# Whole domain $Y$.
region_1000 = {
    'name' : 'Omega',
    'select' : 'all',
}

# Domain $Y_2$.
region_2 = {
    'name' : 'Surface',
    'select' : 'nodes of surface',
}
    
material_1 = {
    'name' : 'm',
    'mode' : 'here',
    'region' : 'Omega',

    'val' : 0.5,
}

material_2 = {
    'name' : 'mat_v',
    'mode' : 'function',
    'region' : 'Omega',

    'function' : 'fun_v',
    'extra_args' : {'mode' : 'r^2'},
}

field_0 = {
    'name' : 'field_Psi',
    'dim' : (1,1),
    'flags' : (),
    'domain' : 'Omega',
    'bases' : {'Omega' : '3_4_P1'}
}

integral_1 = {
    'name' : 'i1',
    'kind' : 'v',
    'quadrature' : 'gauss_o2_d3',
}

variable_1 = {
    'name' : 'Psi',
    'kind' : 'unknown field',
    'field' : 'field_Psi',
    'order' : 0,
}
variable_2 = {
    'name' : 'v',
    'kind' : 'test field',
    'field' : 'field_Psi',
    'dual' : 'Psi',
}
variable_3 = {
    'name' : 'V',
    'kind' : 'parameter field',
    'field' : 'field_Psi',
    'like' : 'Psi',
}

ebc_1 = {
    'name' : 'ZeroSurface',
    'region' : 'Surface',
    'dofs' : {'Psi.0' : 0.0},
}

equations = {
    'lhs' : """  dw_laplace.i1.Omega( m.val, v, Psi )
               + dw_mass_scalar_variable.i1.Omega( mat_v.V, v, Psi )""",
    'rhs' : """dw_mass_scalar.i1.Omega( v, Psi )""",
}

solver_2 = {
    'name' : 'eigen1',
    'kind' : 'eig.pysparse',

    'tau' : -10.0,
    'eps_a' : 1e-5,
    'i_max' : 150,
    'method' : 'qmrs',
    'verbosity' : 0,
    'strategy' : 1,
}

fe = {
    'chunk_size' : 100000
}

##
# c: 01.02.2008, r: 12.06.2008
def fun_v( ts, coor, region, ig, mode = None ):
    from numpy import zeros_like

    out = {}
    val = zeros_like( coor[:,0] )
    out['V'] = val
    return out
