kwadrat :: [Integer] -> [Integer]
kwadrat [] = []
kwadrat (n:ns) = (n ^ 2) : kwadrat ns