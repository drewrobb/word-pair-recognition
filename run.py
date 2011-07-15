import string, random, subprocess, os

num_tests = 100
path = os.getcwd()+'/images'

letters =  [i for i in string.lower(string.letters)[0:26]]

[letters.remove(c) for c in 'aeiou']
letters = 8 * ''.join(letters)

with open("wordsEn.txt") as word_file:
    real_words = set(word.strip().lower() for word in word_file if len(word.strip()) == 8)


def draw(name, color1, color2, word1, word2, i ):
    pos1 = '100,100'
    mid  = '400,100'
    pos2 = '600,100'

    cmd = """\
    convert -font Inconsolata-Medium -pointsize 25 \
    -fill black -draw 'text %s "%s"' \
    -fill %s -draw 'text %s "%s"' \
    -fill %s -draw 'text %s "%s"' %s/../template.png %s
    """

    args = (mid, i, color1, pos1, word1, color2, pos2, word2, path, name)

    subprocess.Popen(cmd % args, shell = True).wait()


filenames = []

for i in range(1,num_tests+1):
    print i
    words = []
    words.append(''.join(random.sample(letters, 8)))
    words.append(random.sample(real_words, 1)[0])

    color = 'black'
    color1 = color
    color2 = color
    if random.random() < 0.5:
        words.reverse()
        color1  = 'red'
    else:
        color2 = 'red'

    fn1 = '%s/q%s.png' % (path, i)
    draw(fn1, color, color, words[0], words[1], i)
    filenames.append(fn1)

    fn2 = '%s/q%sb.png' % (path, i)
    draw(fn2, color1, color2,  words[0], words[1], i)
    filenames.append(fn2)

print 'making gif...'
subprocess.Popen('convert -delay 80 -loop 0 %s %s/../output.gif' % (' '.join(filenames), path) , shell = True).wait()