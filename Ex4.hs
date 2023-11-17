addOneList' lst = map (\x -> x + 1) lst

-- Función para eliminar elementos de una lista basados en otra lista de elementos a borrar
eliminarElementos :: Eq a => [a] -> [a] -> [a]
  eliminarElementos lista [] = lista  -- Caso base: si la lista de elementos a borrar está vacía, retornar la lista original
  eliminarElementos lista (x:xs) = eliminarElementos (filter (\elem -> elem /= x) lista) xs

filtrarElementos :: Eq a => [a] -> [a] -> [a]
  filtrarElementos lista [] = lista
  filtrar elementos (x:xs) = eliminarElementos
-- Ejemplo de lista inicial y lista de elementos a borrar
listaInicial :: [String]
listaInicial = ["rojo", "verde", "azul", "amarillo", "gris", "blanco", "negro"]

elementosABorrar :: [String]
elementosABorrar = ["amarillo", "café", "blanco"]

-- Función main para probar la eliminación de elementos
main :: IO ()
main = do
    putStrLn "Lista inicial:"
    print listaInicial

    putStrLn "Lista de elementos a borrar:"
    print elementosABorrar

    let listaResultante = eliminarElementos listaInicial elementosABorrar

    putStrLn "\nLista resultante después de eliminar elementos:"
    print listaResultante
