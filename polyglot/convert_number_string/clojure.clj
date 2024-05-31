(ns polyglot.convert-number-string.clojure)

(defn ->english [n]
  (cond
    (zero? n) "Zero"
    (< n 20) (nth ["Zero" "One" "Two" "Three" "Four" "Five" "Six" "Seven" "Eight" "Nine" "Ten" "Eleven" "Twelve" "Thirteen" "Fourteen" "Fifteen" "Sixteen" "Seventeen" "Eighteen" "Nineteen"] n)
    (< n 100) (str (nth ["Twenty" "Thirty" "Forty" "Fifty" "Sixty" "Seventy" "Eighty" "Ninety"] (- (quot n 10) 2)) " " (->english (mod n 10)))
    (< n 1000) (str (->english (quot n 100)) " Hundred " (->english (mod n 100)))
    (< n 1000000) (str (->english (quot n 1000)) " Thousand " (->english (mod n 1000)))
    (< n 1000000000) (str (->english (quot n 1000000)) " Million " (->english (mod n 1000000)))
    (< n 1000000000000)(str (->english (quot n 1000000000)) " Billion " (->english (mod n 1000000000)))
    :else "Number is too large"))


(comment
  (->english 0)
  (->english 1000)
  (->english 234)
  (->english 312)
  (->english 999999999999))