import boto3
import sys

client = boto3.client('ssm')

path = sys.argv[1]

params = client.get_parameters_by_path(Path=path, Recursive=True)

for param in params['Parameters']:
    print(f'{param["Name"].replace(path, "SSM_"+path[path.rfind("/")+1:]).replace("/","_").upper()}="{param["Value"]}"')
