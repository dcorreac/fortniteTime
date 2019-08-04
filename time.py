import requests

def fortnite_time(userName):
    header = {"Authorization": 'ab54574fd188389b77c181bd7037ac6a' }
    response = requests.get('https://fortnite-api.theapinetwork.com/users/id?username=' + userName, headers = header)
    user_info = str(response.content)
    userID = user_info.split('uid":"')[1].split('"')[0]

    response2 = requests.get('https://fortnite-api.theapinetwork.com/prod09/users/public/br_stats_v2?user_id=' + userID, headers = header)

    print(str(response2.content),  file=open( userName + '.txt', 'w'))


    myFile = open( userName + ".txt") # get a file handle
    myText= myFile.read() # read the file to variable
    myFile.close() # close file handle
    minSplit = myText.split('minutesplayed":')
    totalMinutes = 0 
    skip = False
    for item in minSplit:
        if(skip == False):
            skip = True
        else:
            totalMinutes = totalMinutes +  int(item.split(',')[0])
    return(totalMinutes/(60*24))



print(fortnite_time('Xxflash18Xx'))