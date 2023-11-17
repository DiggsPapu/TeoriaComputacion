import Data.List (sortBy)
import Data.Ord (comparing)

listaDiccionarios :: [[(String, String)]]
listaDiccionarios =
    [ [ ("make", "Nokia"), ("model", "216"), ("color", "Black") ]
    , [ ("make", "Apple"), ("model", "2"), ("color", "Silver") ]
    , [ ("make", "Huawei"), ("model", "50"), ("color", "Gold") ]
    , [ ("make", "Samsung"), ("model", "7"), ("color", "Blue") ]
    ]

ordenarPorKey :: String -> [[(String, String)]] -> [[(String, String)]]
ordenarPorKey key diccionarios =
    sortBy (comparing (\dic -> lookupOrDefault key dic)) diccionarios
    where
        lookupOrDefault k dic = case lookup k dic of
            Just v -> v
            Nothing -> ""

main :: IO ()
main = do
    let claveOrdenamiento = "model"
    let listaOrdenada = ordenarPorKey claveOrdenamiento listaDiccionarios
    print listaOrdenada