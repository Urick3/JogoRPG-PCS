import random
from character import Character

print("SEJA BEM-VINDO AO SONS OF ALARIA, É UMA PRAZER RECEBER VOCÊ AQUI...VAMOS CRIAR UM PERSONAGEM?")
print("MAS FIQUE ATENTO! ALGUNS PERSONAGENS PODEM RECEBER ALGO A MAIS DE ACORDO COM SUA RAÇA!")
print("\n")
name = input("OLÁ COMBATENTE, DIGITE O NOME DO SEU PERSONAGEM: ")

print("TEMOS ALGUMAS RAÇAS DISPONÍVEIS!")
print("1- Anão (+2 em constituição)")
print("2- Elfo (+2 em posição de destaque)")
print("3- Humano (+1 em todos os atributos)")
print("4- Bárbaro (+2 em destreza)")
print("5- Draconato (+2 em força e +1 em carisma)")
print("6- Gnome (+2 em inteligência)")
print("7- Ladrão (+1 em inteligência e +2 em carisma)")
print("\n")

classes = {
   1:"Anão",
    2:"Elfo",
    3:"Humano",
    4:"Bárbaro",
    5:"Dragonato",
    6:"Gnomo",
    7:"Ladrão",
}

race = 0

while race <= 0 or race > 8:
    race = int(input("DIGITE O VALOR DA RAÇA DO SEU PERSONAGEM: "))
    if race < 8:
     print()
    else:
        print("DIGITE UM VALOR DE RAÇA VÁLIDO, DIGITE UM VALOR DE 1 A 8!")


strength = random.randint(0, 8)
dexterity = random.randint(0, 8)
constitution = random.randint(0, 8)
wisdom = random.randint(0, 8)
intelligence = random.randint(0, 8)
charisma = random.randint(0, 8)

sub_race = None

match race:
    case 1:
        constitution += 2
        print("CERTO, VAMOS ESCOLHER SUA RAÇA")
        print("1- Anão da Colina (+1 de sabedoria)")
        print("2- Anão da Montanha (+2 de força)")
        sub_race_choice = int(input("ÓTIMO, AGORA DIGITE UM NÚMERO PARA A SUB-RAÇA OU DIGITE OUTRO VALOR PARA NÃO ESCOLHER UMA SUB-RAÇA"))
        if sub_race_choice == 1:
            wisdom += 1
            sub_race = "Anão da Colina"
        elif sub_race_choice == 2:
            strength += 2
            sub_race = "Anão da Montanha"

    case 2:
        dexterity += 2
        print("BELEZA, AGORA VAMOS ESCOLHER UMA SUB-RAÇA OU DIGITE OUTRO VALOR PARA NÃO ESCOLHER UMA SUB-RAÇA:")
        print("1- Alto Elfo (+1 de inteligência)")
        print("2- Elfo da Floresta (+1 de sabedoria)")
        print("3- Elfo Negro (+1 de carisma)")
        sub_race_choice = int(input())
        if sub_race_choice == 1:
            intelligence += 1
            sub_race = "Alto Elfo"
        elif sub_race_choice == 2:
            wisdom += 1
            sub_race = "Elfo da Floresta"
        elif sub_race_choice == 2:
            charisma += 1
            sub_race = "Elfo Negro"

    case 4:
        dexterity += 2
        print("BELEZA, AGORA VAMOS ESCOLHER UMA SUB-RAÇA OU DIGITE OUTRO VALOR PARA NÃO ESCOLHER UMA SUB-RAÇA:")
        print("1- Pés Leves (+1 em carisma)")
        print("2- Robusto (+1 em constituição)")
        sub_race_choice = int(input())
        if sub_race_choice == 1:
            charisma += 1
            sub_race = "Pés Leves"
        elif sub_race_choice == 2:
            constitution += 1
            sub_race = "Robusto"

    case 6:
        intelligence += 2
        print("BELEZA, AGORA VAMOS ESCOLHER UMA SUB-RAÇA OU DIGITE OUTRO VALOR PARA NÃO ESCOLHER UMA SUB-RAÇA:")
        print("1- Gnomo da Floresta  (+1 em destreza)")
        print("2- Gnomo da Pedra (+1 em constituição)")
        sub_race_choice = int(input())
        if sub_race_choice == 1:
            dexterity += 1
            sub_race = "Gnomo da Floresta "
        elif sub_race_choice == 2:
            constitution += 1
            sub_race = "Gnomo da Pedra"

character = Character(name, race)
character.attributes['Strength'].value = strength
character.attributes['Dexterity'].value = dexterity
character.attributes['Constitution'].value = constitution
character.attributes['Wisdom'].value = wisdom
character.attributes['Intelligence'].value = intelligence
character.attributes['Charisma'].value = charisma

print("\nESTAS SÃO AS CARACTERÍSTICAS DO SEU PERSONAGEM")
print(f"Nome: {character.name}")
print(f"Classe: {classes[race]}")
if sub_race:
    print(f"Sub-Classe: {sub_race}")
print(f"Força: {character.attributes['Strength'].value} ({character.get_attribute_status('Strength')})")
print(f"Destreza: {character.attributes['Dexterity'].value} ({character.get_attribute_status('Dexterity')})")
print(f"Constituição: {character.attributes['Constitution'].value} ({character.get_attribute_status('Constitution')})")
print(f"Sabedoria: {character.attributes['Wisdom'].value} ({character.get_attribute_status('Wisdom')})")
print(f"Inteligência: {character.attributes['Intelligence'].value} ({character.get_attribute_status('Intelligence')})")
print(f"Carisma: {character.attributes['Charisma'].value} ({character.get_attribute_status('Charisma')})")