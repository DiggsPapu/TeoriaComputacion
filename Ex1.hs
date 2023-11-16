import Data.List (sortBy)
import Data.Ord (comparing)

-- Lista de diccionarios
listaDiccionarios :: [[(String, String)]]
listaDiccionarios =
    [ [ ("make", "Nokia"), ("model", "216"), ("color", "Black") ]
    , [ ("make", "Apple"), ("model", "2"), ("color", "Silver") ]
    , [ ("make", "Huawei"), ("model", "50"), ("color", "Gold") ]
    , [ ("make", "Samsung"), ("model", "7"), ("color", "Blue") ]
    ]

-- Función para ordenar la lista de diccionarios por una clave específica
ordenarPorKey :: String -> [[(String, String)]] -> [[(String, String)]]
ordenarPorKey key diccionarios =
    sortBy (comparing (\dic -> lookupOrDefault key dic)) diccionarios
    where
        lookupOrDefault k dic = case lookup k dic of
            Just v -> v
            Nothing -> ""

-- Función main para probar el ordenamiento
main :: IO ()
main = do
    putStrLn "Lista de diccionarios antes de ordenar:"
    mapM_ print listaDiccionarios

    let claveOrdenamiento = "color"  -- Clave por la que se ordenará la lista de diccionarios
    let listaOrdenada = ordenarPorKey claveOrdenamiento listaDiccionarios

    putStrLn $ "\nLista de diccionarios ordenada por la clave '" ++ claveOrdenamiento ++ "':"
    mapM_ print listaOrdenada
