import sys

def create_cmp(arq):
    lista = []

    open_arq = open(arq, "r")

    for line in open_arq:
        lista.append(line)

    return lista

def main():
    if len(sys.argv) > 2:
        input1 = sys.argv[1]
        input2 = sys.argv[2]
        dim = sys.argv[3]
        k = sys.argv[4]
    else:
        print("invalid args!!!")
        print("usage: <input_1> <input_2>\n") 
        return
    
    list_1 = create_cmp(input1)
    list_2 = create_cmp(input2)

    count = 0
    for i in range(len(list_1)):
        if(list_1[i] != list_2[i]):
            count += 1

    print(dim+","+k+","+str(count/(len(list_1)-1)))

    #print("points total    = "+str(len(list_1)))
    #print("qtd points diff = "+str(count))

if __name__ == "__main__":
    main()