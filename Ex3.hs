transposeMatrix :: [[a]] -> [[a]]
transpose ([]:_) = []
transposeMatrix matrix = if null (head matrix) then [] 
                         else (map head matrix) : transposeMatrix (map tail matrix)
miMatriz :: [[Int]]
miMatriz =
    [ [1, 2, 3, 1]
    , [4, 5, 6, 0]
    , [7, 8, 9, -1]
    ]
main :: IO ()
main = do
    let transpuesta = transposeMatrix miMatriz
    print transpuesta