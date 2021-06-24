<!-- run actions -->
python -m rasa_core_sdk.endpoint --actions actions

<!-- run file train_dialog -->
python train_dialog.py

<!-- run file test_dialog -->
python test_dialog.py

<!-- rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
rasa run actions
sudo /opt/lampp/lampp start -->
