# Notifications

## Create a notification

**Parameters**

| Field       | Type       | Required | Description               |
|-------------|------------|----------|---------------------------|
| title       | char (50)  | yes      | Title of the notification |
| description | char (100) | no       | Body of the notification  |
|             |            |          |                           |

**Endpoint**

```
POST /api/notifications
```

**Request**

```json
{
  "title": "new title",
  "description": "some line of text about notification"
}
```

**Response**

Status: `201 Created`

```json
{
  "title": "new title",
  "description": "some line of text about notification"
}
```

# Subscriptions

## Create a subscription

**Parameters**


| Field               | Type       | Required | Description                                              |
|---------------------|------------|----------|----------------------------------------------------------|
| push_service_url    | char (200) | yes      | Push Service Endpoint to make web push protocol requests |
| subscription_auth   | char (200) | yes      | private "p256dh" client key from the subscription data   |
| subscription_secret | char (100) | yes      | public "auth" client key from the subscription data      |
|                     |            |          |                                                          |


**Endpoint**

```
POST /api/subscriptions
```

**Request**

```json
{
  "push_service_url": "<https://some.pushservice.com/something-unique>",
  "client_private_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
  "client_public_key": "FPssNDTKnInHVndSTdbKFw=="
}
```

**Response**

Status: `201 Created`

```json
{
  "id": "070af5d3-03a1-4a38-9a75-5b76de8826d2",
  "push_service_url": "<https://some.pushservice.com/something-unique>",
  "client_private_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
  "client_public_key": "FPssNDTKnInHVndSTdbKFw==",
  "created_at": "2022-08-10T17:30:42Z"
}
```
