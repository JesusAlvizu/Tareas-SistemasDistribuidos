import numpy as np

def rot_x(x, y, z, beta):
    '''
    Rota el vector (x, y, z) un ángulo beta (en radianes) respecto al eje X.

    Parameters:
        x (float): coordenada x
        y (float): coordenada y
        z (float): coordenada z
        beta (float): ángulo de rotación en radianes

    Returns:
        numpy.array: vector rotado
    '''
    p = np.array([x, y, z])
    R = np.array([
        [1, 0, 0],
        [0, np.cos(beta), -np.sin(beta)],
        [0, np.sin(beta), np.cos(beta)]
    ])
    return R @ p

def rot_y(x, y, z, beta):
    '''
    Rota el vector (x, y, z) un ángulo beta (en radianes) respecto al eje Y.

    Parameters:
        x (float): coordenada x
        y (float): coordenada y
        z (float): coordenada z
        beta (float): ángulo de rotación en radianes

    Returns:
        numpy.array: vector rotado
    '''
    p = np.array([x, y, z])
    R = np.array([
        [np.cos(beta), 0, np.sin(beta)],
        [0, 1, 0],
        [-np.sin(beta), 0, np.cos(beta)]
    ])
    return R @ p

def rot_z(x, y, z, beta):
    '''
    Rota el vector (x, y, z) un ángulo beta (en radianes) respecto al eje Z.

    Parameters:
        x (float): coordenada x
        y (float): coordenada y
        z (float): coordenada z
        beta (float): ángulo de rotación en radianes

    Returns:
        numpy.array: vector rotado
    '''
    p = np.array([x, y, z])
    R = np.array([
        [np.cos(beta), -np.sin(beta), 0],
        [np.sin(beta), np.cos(beta), 0],
        [0, 0, 1]
    ])
    return R @ p

def rotar(x, y, z, beta, axis):
    '''
    Rota el vector (x, y, z) un ángulo beta (en radianes) respecto al eje especificado.

    Parameters:
        x (float): coordenada x
        y (float): coordenada y
        z (float): coordenada z
        beta (float): ángulo de rotación en radianes
        axis (string): eje de rotación; puede ser 'x', 'y' o 'z'

    Returns:
        numpy.array: vector rotado
    '''
    if axis == 'x':
        return rot_x(x, y, z, beta)
    elif axis == 'y':
        return rot_y(x, y, z, beta)
    elif axis == 'z':
        return rot_z(x, y, z, beta)
    else:
        raise ValueError("El eje debe ser 'x', 'y' o 'z'.")

if __name__ == "__main__":
    # Ejemplo: rotar el vector (1, 0, 0) 90 grados (pi/2 radianes) alrededor del eje y 
    import math
    v_rotado = rotar(1, 0, 0, math.pi/2, 'y')
    print("Vector rotado:", v_rotado)