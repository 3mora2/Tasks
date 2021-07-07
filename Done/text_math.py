import itertools

method_first = []
method = []


def Math_do(a, b, c, d, res, f=False):
    for p in itertools.product(('**-1 ', '**-2 ', '**-3 ', '**-4 ', '**0 ', '**1 ', '**2 ', '**3 ', '**4 ', '**-1/2 ',
                                '**-1/3 ', '**-1/4 ', '**1/2 ', '**1/3 ', '**1/4 '),
                               repeat=4):
        ns = [str(a) + p[0], str(b) + p[1], str(c) + p[2], str(d) + p[3]]
        for e in itertools.product(('* ', '- ', '+ ', '// ', '/ '), repeat=3):
            m = str(ns[0]) + ' '.join([x + str(y) for x, y in zip(e, ns[1:])])
            if eval(m) == res:
                print(m, ' = ', eval(m))
                if f:
                    method_first.append((p, e))
                else:
                    if (p, e) in method_first:
                        method.append((p, e))
                        print(method)
                        break
        if len(method) != 0:
            break

def ress(a, b, c, d):
    e = method[0][1]
    p = method[0][0]
    ns = [str(a) + p[0], str(b) + p[1], str(c) + p[2], str(d) + p[3]]
    m = str(ns[0]) + ' '.join([x + str(y) for x, y in zip(e, ns[1:])])
    print(eval(m))

Math_do(5, 6, 7, 2, 375, True)
Math_do(2, 5, 6, 6, 226)

ress(2, 5, 6, 6)
# Math_do(17500, 17366, 17381, 17457, 17465)
# print('**********************************')
# Math_do(17458, 17410, 17447, 17419, 17381)
# print('**********************************')
# Math_do(17450, 17403, 17406, 17447, 17419)
# print('**********************************')
# Math_do(17486, 17363, 17419, 17381, 17457)

'''
المسألة الاولي 
أ = 17500
ب = 17366
ت = 17381
د = 17457

الناتج = 17465

_____

المسألة الثانيه
أ = 17458
ب = 17410
ت = 17447
د = 17419

الناتج = 17381
_____

المسألة الثالثه
أ = 17450
ب = 17403
ت = 17406
د = 17447

الناتج = 17419

______

المسألة الرابعه
أ = 17486
ب = 17363
ت = 17419
د = 17381

الناتج = 17457


_____

المسألة الخامسه
أ = 17463
ب = 17281
ت = 17459
د = 17292

الناتج = ؟؟؟؟؟؟
'''
