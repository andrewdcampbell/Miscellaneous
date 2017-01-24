(define (draw times)
  (bgcolor (rgb 0 0 0))
  (speed 0)
  (move 1 times 1 0 0)
  (draw (- times 18)))

; Try 89 for spirals
(define (move accum limit r g b)
  (cond ((< accum limit)
		(cond
        	((and (> r b) (= g 0) (< b 0.98)) (define b (+ b 0.02)))
        	((and (> r 0.05) (= g 0)) (define r (- r 0.02)))
        	((and (< g 0.98) (< r .1)) (define g (+ g 0.02)) (define r 0))
        	((> b 0.05) (define b (- b 0.02)))
        	((< r 0.98) (define r (+ r 0.02)) (define b 0))
        	((> g 0.05) (define g (- g 0.02)))
        	(else (define g 0))
      		)
         (color (rgb r g b))
         (fd (+ (* 0.8 accum)
                (* 0.00000075 (* accum (* accum accum)))))
         (rt 160)
         (define accum (+ 1 accum))
         (move accum limit r g b))))


(hideturtle)
(draw 386)

