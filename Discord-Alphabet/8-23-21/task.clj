(defn fun [n]
    (let [num_five (mod (* -1 n) 3)]
        (let [num_three (/ (- n (* 5 num_five)) 3)]
            (println n ":" num_three num_five)
        )
    )
)
(fun 11)
(fun 15)
(fun 29)
(fun 1562)