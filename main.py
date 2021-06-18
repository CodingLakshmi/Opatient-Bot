import os
import discord
import math
import random

client = discord.Client()
my_secret = os.environ['TOKEN']

def format_array(array):
  output = ''
  for i in range(len(array)):
    output += array[i]
    output += "\n"
  return output

Pictures = {
  "Images": [
    "https://hivgov-prod-v3.s3.amazonaws.com/s3fs-public/field/image/measles-blog-may1-540.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/4uft.jpg/752px-4uft.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Morbillivirus_measles_infection.jpg/640px-Morbillivirus_measles_infection.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Vial_of_smallpox_vaccine.jpg/640px-Vial_of_smallpox_vaccine.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Injectable_Polio_Vaccine.jpg/640px-Injectable_Polio_Vaccine.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Polio_lores134.jpg/640px-Polio_lores134.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Polio.jpg/640px-Polio.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Coronavirus._SARS-CoV-2.png/640px-Coronavirus._SARS-CoV-2.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Coronavirus_replication_cycle.jpg/640px-Coronavirus_replication_cycle.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/SymptomsofCOVID19.jpg/640px-SymptomsofCOVID19.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Pruritic_rash_COVID.jpg/640px-Pruritic_rash_COVID.jpg",
    "https://www.unicef.org/afghanistan/sites/unicef.org.afghanistan/files/styles/hero_mobile/public/72283548_2399821583588645_2366690180263313408_o.jpg?itok=lwsOsvx8",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGJHeMg1MzgfKTJcGjlvB8nVSR7UDTlLEK2w&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScAa52kbBDnZG70Z1rLbyMr78Bg6Ih13driA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNbzkqZIDGOmgdZmz_JJri1L1oJ24KUv0eHQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJC70uUBdXRiZj2Yi0PLycf8ZLsNng-iogZg&usqp=CAU",
    "https://www.nih.gov/sites/default/files/styles/floated_media_breakpoint-medium/public/news-events/research-matters/2020/20201020-covid.jpg?itok=EYYGAYzj&timestamp=1603197819",
    "https://www.hopkinsmedicine.org/sebin/b/t/SARS-CoV-2%20Virus%20in%20Middle%20Ear%20and%20Mastoid.jpg",
    "https://www.ccjm.org/content/ccjom/87/6/321/F1.large.jpg",
    "https://asm.org/ASM/media/Article-Images/2019/May/ImmuneAmnesia2-5-18-19.png?ext=.png"
  ]
} 

Measles_Symptoms = [
  "Fever",
  "Cough",
  "Runny nose",
  "Conjunctivitis",
  "Rash",
  "Koplik spots"
]

Covid_Symptoms = [
  "Fever (typically over 100 degrees Fahrenheit/ 38 degrees Celsius)",
  "Dry cough",
  "Chills",
  "Fatigue or weakness",
  "Sore throat",
  "Gastrointestinal symptoms, such as diarrhea, vomiting, and abdominal pain",
  "Aches and pains",
  "Headache",
  "Conjunctivitis",
  "Loss of taste or smell",
  "Rash on skin/ skin discoloration",
  "Difficulty breathing/ shortness of breath",
  "Pressure or pain in chest",
  "Loss of speech/ movement ",
]

Smallpox_Symptoms = [
  "Fever",
  "Physical discomfort",
  "Headache",
  "Back pain",
  "Tiredness",
  "Vomiting",
  "Flat red spots",
  "Blisters"
]

Polio_Symptoms = [
  "Sore throat",
  "Fever",
  "Tiredness",
  "Nausea",
  "Headache",
  "Stomach pain",
  "Paralysis",
  "Paresthesia"
]

website = [
  "Opatient is a service that can help you find the online health services you need. We have articles that can inform you about your condition while also suggesting top medical services available online.",
  "https://opatient.lakshmi2021.repl.co/index.html"
]

measles_info = (
  "Measles is a highly infectious disease caused by the rubeola virus, a virus that is spread through air and is so easily transmissible that up to every 9 in 10 people around infected patients can be infected themselves if not wearing proper protection. Measles may cause severe complications as well, especially in infants and young children. Common symptoms of measles include fever, cough, runny nose, red and watery eyes, and a rash. Like many other viral diseases, there is no cure that completely exterminates all traces of the rubeola virus in bodies, but there are MMR vaccines that provide long-term protection. It is advised that the first dose be administered at 12-15 months of age, and the second dose at 4-6 years of age. Today, measles is rare in the US, however, it does still exist in other parts of the world."
)

polio_info = (
  "Poliomyelitis, more commonly known as polio, is a dangerous and potentially life-threatening disease that occurs as a result of contracting poliovirus. Unlike the virus that causes COVID-19, poliovirus is not zoonotic. There are two main forms of transmission of the disease: coming into contact with droplets of saliva from the cough or sneeze of an infected person, or coming into contact with infected feces, whether directly (such as touching your face with feces on your hands) or indirectly (such as putting an object that is contaminated with infected feces near your face.) Those suffering from polio exhibit a wide range of symptoms, the most severe of which is paralysis. Other symptoms, such as paresthesia, tend to predominantly affect muscles, restricting mobility and causing physical discomfort. Paralysis resulting from polio often culminates in death, and even those who have completely recovered from it often relapse into other polio symptoms years later. Polio has largely been eradicated today, and despite the lack of treatment options, there have been vaccines developed to decrease risk of mortality."
)

smallpox_info = (
  "Smallpox is a contagious disease that is caused by the variola virus. It is characterized by physical disfigurements such as small, red spots that eventually become fluid-filled blisters and sores. These lesions eventually scab over, then permanently scar when the scabs peel off. Although a dangerous and potentially fatal disease, smallpox has been eradicated entirely worldwide as of 1980. No cure or treatment method to rid of the disease exists; however, there are vaccines available to help alleviate the severity of symptoms. Smallpox can easily be contracted and is spread both directly and indirectly. Direct transmission of the variola virus involves an infected person releasing droplets of saliva into the air when coughing or sneezing, thereby coming into contact with uninfected individuals. Indirect transmission of the virus involves droplets of saliva from an infected person being released into the air and passing through a ventilation system or other similar means of air circulation to affect others who are not in close proximity to the infected individual."
)

covid_info = (
  "COVID-19 is a contagious respiratory disease caused by the novel coronavirus Sars-Cov2, discovered in the Wuhan region of China in 2019. It has many flu-like symptoms, such as fever, chills, dry cough, and fatigue, to name a few (if you would like more information on symptoms, use the $Covid-symptoms commands). Sars-Cov2 is said to have had a zoonotic origin from bats or another similar animal, and it is highly contagious. People can be infected with the virus via infected moisture droplets that are released into the air when an infected person coughs or sneezes, as well as when they come into contact with virus-contaminated surfaces and objects. No cure has been developed to treat COVID-19; however, mRNA vaccines that prepare our bodies to initiate an antibody response against the virus are in widespread use across the globe in hopes of achieving herd immunity."
)

commands = ['!test', '!commands', '!help', '$covid-symptoms', '$smallpox-symptoms', '$polio-symptoms', '$measles-symptoms', '$images', '$website', '$covid-info', '$measles-info', '$polio-info', '$smallpox-info']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!test'):
    await message.channel.send("testing")

  if message.content.startswith("!commands"):
    await message.channel.send(format_array(commands))
  
  if message.content.startswith("!help"):
    await message.channel.send("This is an informational bot. It is a smaller version of the Opatient website. If you are the kind of person who likes to skim through the whole website to get the answers, you can use this Discord bot to speed up your work. I suggest you use !commands so that you can get a list of commands. From there, you can experiment with all the different commands. Have fun! We hope you enjoy our Opatient bot and website.")

  if message.content.startswith("$website"):
    await message.channel.send(format_array(website))

  if message.content.startswith("$covid-symptoms"):
    await message.channel.send(format_array(Covid_Symptoms))

  if message.content.startswith("$smallpox-symptoms"):
    await message.channel.send(format_array(Smallpox_Symptoms))
  
  if message.content.startswith("$polio-symptoms"):
    await message.channel.send(format_array(Polio_Symptoms))
  
  if message.content.startswith("$measles-symptoms"):
    await message.channel.send(format_array(Polio_Symptoms))

  if message.content.startswith("$images"):
    await message.channel.send(Pictures['Images'][random.randint(0, len(Pictures['Images'])-1)])

  if message.content.startswith("$smallpox-info"):
    await message.channel.send(smallpox_info)

  if message.content.startswith("$covid-info"):
    await message.channel.send(covid_info)

  if message.content.startswith("$polio-info"):
    await message.channel.send(polio_info)

  if message.content.startswith("$measles-info"):
    await message.channel.send(measles_info)
    

client.run(os.getenv('TOKEN'))