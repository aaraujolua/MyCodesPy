students_notes = [10, 30, 91, 100, 60]
students_average = lambda notes: sum(notes) / len(notes) #Fórmula = lambda argumento: regra

print(f'The students average is {students_average(students_notes)}')

#Função para filtrar as notas acima de 80

filter_notes = list(filter(lambda i: i>80, students_notes))
 #Fórmula = função_padrão(função_padrão(lambda argumento: regra, lista))
print(f'The notes above 80 are: {filter_notes}')
