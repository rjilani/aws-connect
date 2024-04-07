import boto3
import json
from utils.fileutil import dateconverter
from utils.fileutil import write_json_file
from utils.fileutil import read_json_file

client = boto3.client('connect')


def list_instances():
    response = client.list_instances(
        MaxResults=123
    )

    json_string = json.dumps(response['InstanceSummaryList'], sort_keys=True, indent=4, default=dateconverter)

    print(json_string)
    write_json_file("data/connect_instnace_info.json", json_string)


def list_contact_flows():
    response = client.list_contact_flows(
        InstanceId='XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ContactFlowTypes=[
            'CONTACT_FLOW'
        ],
        MaxResults=123
    )

    json_string = json.dumps(response, sort_keys=True, indent=4, default=dateconverter)

    print(json_string)
    write_json_file("data/connect_flow_info.json", json_string)


def describe_contact_flow():
    response = client.describe_contact_flow(
        InstanceId='XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ContactFlowId='XXXXXXXXXXXXXXXXXXXXXXXXXXX'
    )

    json_string = json.dumps(response, sort_keys=True, indent=4, default=dateconverter)

    print(json_string)


def create_instances():
    response = client.create_instance(
        IdentityManagementType='CONNECT_MANAGED',
        InstanceAlias='XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        InboundCallsEnabled=True,
        OutboundCallsEnabled=True

    )

    json_string = json.dumps(response, sort_keys=True, indent=4, default=dateconverter)
    print(json_string)


def delete_instances():
    response = client.delete_instance(
        InstanceId='XXXXXXXXXXXXXXXXXXXXXXXXXXX')

    json_string = json.dumps(response, sort_keys=True, indent=4, default=dateconverter)
    print(json_string)


def delete_instance_flow():
    response = client.delete_contact_flow(
        InstanceId='XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ContactFlowId='XXXXXXXXXXXXXXXXXXXXXXXXXXX'
    )
    json_string = json.dumps(response, sort_keys=True, indent=4, default=dateconverter)
    print(json_string)


def list_queues():
    response = client.list_queues(
        InstanceId='XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        QueueTypes=[
            'AGENT', 'STANDARD'
        ],
        MaxResults=123

    )

    json_string = json.dumps(response['QueueSummaryList'], sort_keys=True, indent=4, default=dateconverter)

    print(json_string)
    write_json_file("data/connect_queue_info.json", json_string)


def list_phones():
    response = client.list_phone_numbers(
        InstanceId='XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        MaxResults=123

    )

    json_string = json.dumps(response['PhoneNumberSummaryList'], sort_keys=True, indent=4, default=dateconverter)

    print(json_string)
    write_json_file("data/connect_phone_info.json", json_string)


def create_flow():
    data = read_json_file("data/CloudifiedNow Inbound Flow.json")

    print(type(data))

    json_string = json.dumps(data, sort_keys=True, indent=4, default=dateconverter)
    # print(json_string)

    response = client.create_contact_flow(
        InstanceId='XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        Name='XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        Type='CONTACT_FLOW',
        Description='XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        Content=json_string

    )


def associate_phone_number_to_contact_flow():
    response = client.associate_phone_number_contact_flow(
        PhoneNumberId='XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        InstanceId='XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ContactFlowId='XXXXXXXXXXXXXXXXXXXXXXXXXXX'
    )

    json_string = json.dumps(response, sort_keys=True, indent=4, default=dateconverter)

    print(json_string)


if __name__ == '__main__':
    list_instances()
    # list_queues()
    # list_phones()
    # create_instances()
    # delete_instances()
    # list_contact_flows()
    # delete_instance_flow()
    # create_flow()
    # describe_contact_flow()
    associate_phone_number_to_contact_flow()
