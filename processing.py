def process_data(input_file,output_file):
    with open(input_file,'r') as file:
        data =file.readlines()

        #Performing calculations on the data total and average 
    
    numbers=[float(line.strip()) for line in data]
    total=sum(numbers)
    average=total/len(numbers)

    # writing resultant data in outputfile

    with open(output_file,'w') as file:
        file.write(f"Total :{total}\n")
        file.write(f'Average:{average}\n')

process_data('input.txt','output.txt')