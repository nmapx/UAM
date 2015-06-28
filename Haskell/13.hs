usunzlisty _ [] = [] 
usunzlisty a (b:bc) | a == b = bc 
                    | otherwise = b : usunzlisty a bc