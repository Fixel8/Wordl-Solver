print("wordl solveer >w<")
def loop():
    with open("oxytocin.txt","r") as f:
        words = [line.strip().lower() for line in f if len(line.strip())==5]
    print()
    greens_input=input().ljust(5);greens=[(i,j) for i,j in enumerate(greens_input.lower()) if j!=' ']
    yellows=[]
    while True:
        line=input().ljust(5)
        if line.strip()=='':break
        yellows+=[(i,j) for i,j in enumerate(line.lower()) if j!=' ']
    possible=[];used_letters=set("chunkfjordgympswaltzvibex");allowed_letters=set(j for _,j in greens+yellows)|{'q'}
    for word in words:
        if any(word[i]!=j for i,j in greens):continue
        if any(word[i]==j or j not in word for i,j in yellows):continue
        if any(j not in allowed_letters for j in word):continue
        possible.append(word)
    print(f"Possible words ({len(possible)}):")
    for w in possible:print(w);loop()
loop()