potega x y = (if y == 0 then 1 else if y > 0 then x^y else 1/(x^y))

potegar x y = (if y == 0 then 1 else x * potegar x (y-1))