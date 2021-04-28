sentence = input('enter>')
words = sentence.split(',')
emojis = {

    ':)': '😁😁',
    ':(': '😡😡'
}
output = ''
for word in words:
    output += emojis.get(word, word)+''
print(output)

