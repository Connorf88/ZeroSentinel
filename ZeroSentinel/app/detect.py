import pandas as pd
from sklearn.ensemble import IsolationForest
import json

df = pd.read_csv('data/syslog.csv')
df['src_encoded'] = df['source_ip'].astype('category').cat.codes
df['action_encoded'] = df['action'].astype('category').cat.codes

model = IsolationForest(contamination=0.2)
df['anomaly'] = model.fit_predict(df[['src_encoded', 'action_encoded']])

alerts = df[df['anomaly'] == -1]
print(json.dumps(alerts.to_dict(orient='records'), indent=2))

