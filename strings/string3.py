# formatting strings
# %d 정수, %s 문자열, %c 문자1개
# %f 부동소수, %o 8진수, %x 16진수, %% Literal % 문자 %자체

num = 3
str = "four"
a = "I eat %d apples." % 5
b = 'I had %s bananas.' %"two"
c = 'I ate %d apples, so i was sick for %s days.' %(num, str)
print(a)
print(b)
print(c)

# use format function
ex1 = "i eat {0} apples.".format(4)
ex2 = "There are {0} apples.".format("two")
ex3 = "I had {0} bananas.".format(num)
ex4 = "i ate {0} apples, and then i had {1} bananas.".format(num, 2)
print(ex1)
print(ex2)
print(ex3)
print(ex4)