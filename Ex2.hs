potenciaN :: Int -> [Int] -> [Int]
potenciaN n = map (\x -> x ^ n)
main :: IO ()
main = do
    let listaEnteros = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
    let exponente = 10

    putStrLn "Lista de enteros:"
    print listaEnteros

    let resultado = potenciaN exponente listaEnteros

    putStrLn $ "\nPotencia " ++ show exponente ++ " de cada elemento:"
    print resultado
