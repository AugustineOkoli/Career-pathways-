from django.shortcuts import render
from django.http import HttpResponse
import joblib

# Create your views here.
def home(request):
  return render(request, 'home.html')

def prediction(request):
  return render(request, 'prediction.html')

def result(request):
    # Load the classifier
    cls = joblib.load('C:\\Users\\Okoli Augustine\\Desktop\\project\\Donsino Project\\CareerPrediction\\hybridmodel.pkl')

    # Get user input from the form
    lis = [
        request.GET['ML'],
        request.GET['YOE:ML'],
        request.GET['DL'],
        request.GET['YOE:DL'],
        request.GET['Image Processing'],
        request.GET['YOE:Image Processing'],
        request.GET['Python'],
        request.GET['YOE:python'],
        request.GET['Java'],
        request.GET['YOE:Java'],
        request.GET['C'],
        request.GET['YOE:C'],
        request.GET['HTML'],
        request.GET['YOE:HTML'],
        request.GET['CSS'],
        request.GET['YOE:CSS'],
        request.GET['MYSQL'],
         request.GET['YOE:MYSQL'],
        request.GET['NLP'],
        request.GET['YOE:NLP'],
        request.GET['CGPA'],
        
    ]

    # Predict the career
    predicted_career_name = cls.predict([lis])[0]  # Extracting the predicted career name from the array

    # Dictionary mapping career codes to names
    career_names = {
     0: 'Full stack Developer',
     1: 'AIML engineer',
     2: 'Software Developer',
     3:'Developer',
     4: 'Data analyst',
     5:'Tester',
     6:'UI/UX Designer',
     7:'Front End Developer',
     8:'software engineer',
     9:'Manager',
    10:'software architect',
    11:'Team Lead'
}
    


# Get the name of the predicted career
    predicted_career = career_names.get(predicted_career_name, 'Unknown')

    return render(request, 'result.html', {'predicted_career': predicted_career})