text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(':')
bite=text[pos+5:]
float(bite)
print(bite)