usunNth n xs | n > 0 = take (n-1) xs ++ drop n xs
usunNth n xs | n > 0 = take (n-1) xs ++ drop n xs
let (ys,zs) = splitAt n xs in ys ++ (tail zs)