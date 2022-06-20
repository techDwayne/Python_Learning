#ex 6_05
text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(':')
ipos=text[pos+5:]
float(ipos)
print(ipos)