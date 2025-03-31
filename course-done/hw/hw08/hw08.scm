(define (ascending? s)
  (if (or (null? s) (null? (cdr s)))
      #t
      (and (<= (car s) (car (cdr s))) (ascending? (cdr s)))))

(define (my-filter pred s)
  (cond ((null? s) '())
        ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
        (else (my-filter pred (cdr s))))
)

(define (interleave lst1 lst2) 
  (cond 
    ((null? lst1) lst2)
    ((null? lst2) lst1)
    (else (cons (car lst1) (interleave lst2 (cdr lst1))))
  ))

(define (no-repeats s)
  (if (null? s) s
    (cons (car s)
      (no-repeats (filter (lambda (x) (not (= (car s) x))) (cdr s))))))
