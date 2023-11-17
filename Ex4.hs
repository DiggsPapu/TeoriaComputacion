eliminarElementos :: Eq a => [a] -> [a] -> [a]
eliminarElementos listaAFiltrar listaEliminar = filter (`notElem` listaEliminar) listaAFiltrar

main :: IO ()
main = do
    let listaInicial = ["rojo", "verde", "azul", "amarillo", "gris", "blanco", "negro"]
    let elementosABorrar = ["amarillo", "azul", "blanco"]
    let listaResultante = eliminarElementos listaInicial elementosABorrar
    print listaResultante
