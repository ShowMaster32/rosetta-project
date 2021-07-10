import Data.Char (toLower)

isPalindrome :: Eq a => [a] -> Bool
isPalindrome = (==) <*> reverse

-- Alternatively, comparing just the first half with the reversed latter half
isPal :: Eq a => [a] -> Bool
isPal s =
  let (q, r) = quotRem (length s) 2
  in take q s == reverse (drop (q + r) s)

sample :: String
sample = "In girum imus nocte et consumimur igni"

prepared :: String -> String
prepared = filter (' ' /=) . fmap toLower

main :: IO ()
main = print $ [isPalindrome, isPal] <*> [prepared sample]
