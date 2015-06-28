repl [] = []
repl [z] = [z]
repl (z:lista) = (last lista : init lista) ++ [z]