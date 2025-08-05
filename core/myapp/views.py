import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import ImageSerializer
from .Classifier import Classification

db_logger = logging.getLogger(__name__)
db_logger = logging.getLogger("db_logger")
console_logger = logging.getLogger("console_logger")

class PredictImage(APIView):
    
    def post(self, request): # python310 manage.py runserver 8001
        data = request.data
        if "image" not in data or "image" not in request.FILES:
            db_logger.error("Image was not given in the API")
            return Response({"message":"Image not found"},
                            status=status.HTTP_404_NOT_FOUND)
            
        try:
            Image = request.FILES.get('image')
            console_logger.debug("preprocessing image")
            Processed_img = Classification.preprocess(img=Image)

            classification = Classification()
            console_logger.debug("Inserting Image to the model for prediction")
            predicted_number, accuracy_score = classification.predict(img=Processed_img)

            db_logger.info(f"Image Predicted Sucessfully with digit {predicted_number}")
            console_logger.info(f"Image Predicted Sucessfully with digit {predicted_number}")
            
            Image.seek(0)
            data['image'] = Image
            data['predicted_digit'] = int(predicted_number)
            data['prediction_score'] = float(accuracy_score)

            serializer = ImageSerializer(data=data)
            if serializer.is_valid():
                
                serializer.save()
                db_logger.info(f"Data Saved into DB with digit{predicted_number} of accuracy score {accuracy_score:.2f}")
                return Response({"message":f"Digit predicted => {predicted_number} with accuracy {accuracy_score:.2f} and saved Sucessfully"},
                                status=status.HTTP_201_CREATED)
            else:
                db_logger.warning(f"Digit predicted => {predicted_number}  but data not saved in the database")
                return Response({"message":f"Digit predicted => {predicted_number} but not saved in Database",
                                    "error":serializer.error_messages},
                                status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            db_logger.critical(str(e))
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)