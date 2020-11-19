name = 'danil'
name + "is 26 years old"
print(name)
sent = "is 26 years %s old"
print(sent)
print(sent %name )

print('-'*20)

sent = "%s %s is a programmer python developer"
print(sent%("danil","syah"))

sent = "%s is %d years old"
print(sent%("haykal", 2))
sent2 = sent%("haykal", 2)
print(sent2)
