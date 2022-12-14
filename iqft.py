def iqft(n: int, qubits: int, circuit):
    #Swap the qubits
    for i in range(n//2):
        circuit.append(SWAP(qubits[i],qubits[n-i-1]), strategy = InsertStrategy.NEW)    
    
    for i in range(n-1,-1,-1):
        #Apply CR_k gates where j is the control and i is the target
        k=n-i
        for j in range(n-1,i,-1):
            #Define and apply CR_k gate  
            crk = CZPowGate(exponent = -2/2**(k))
            circuit.append(crk(qubits[j],qubits[i]),strategy = InsertStrategy.NEW)
            k-=1 #Increment k at each step
    
        #Apply Hadamard to the qubit
        circuit.append(H(qubits[i]), strategy = InsertStrategy.NEW)