potenciaN :: Int -> [Int] -> [Int]
potenciaN result = map (^ result) 
main :: IO ()
main = do
    let listaEnteros = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
    let exponente = 3
    let result = potenciaN exponente listaEnteros
    print result