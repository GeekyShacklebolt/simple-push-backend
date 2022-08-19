# Notifications

## Create a notification

**Parameters**

| Field       | Type       | Required | Description                                                                    |
|-------------|------------|----------|--------------------------------------------------------------------------------|
| id          | UUID       | yes      | (response only attribute) UUID of the Notification Object                      |
| title       | char (50)  | yes      | Title of the notification                                                      |
| description | char (100) | no       | Body of the notification                                                       |
| created_at  | datetime   | yes      | (response only attribute) Timestamp of when the Notification object is created |
|             |            |          |                                                                                |

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
  "id": "122115d3-03a1-4a38-9a75-5b76de8826d2",
  "title": "new title",
  "description": "some line of text about notification",
  "created_at": "2022-08-10T17:30:42Z"
}
```

## List Notifications

**Endpoint**

```
GET /api/notifications
```

**Response**

Status: `200 OK`

```json
[
  {
    "id": "122115d3-03a1-4a38-9a75-5b76de8826d2",
    "title": "new title",
    "description": "some line of text about notification",
    "created_at": "2022-08-10T17:30:42Z"
  }
]
```

# Subscriptions

## Create a subscription

**Parameters**


| Field                   | Type       | Required | Description                                                                    |
|-------------------------|------------|----------|--------------------------------------------------------------------------------|
| id                      | UUID       | yes      | (response only attribute) UUID of the Subscription object                      |
| push_service_url        | char (200) | yes      | Push Service Endpoint to make web push protocol requests                       |
| subscription_public_key | char (200) | yes      | public "p256dh" client key from the subscription data                          |
| subscription_auth       | char (100) | yes      | private "auth" client key from the subscription data                           |
| created_at              | datetime   | yes      | (response only attribute) Timestamp of when the Subscription object is created |
|                         |            |          |                                                                                |


**Endpoint**

```
POST /api/subscriptions
```

**Request**

```json
{
  "push_service_url": "<https://some.pushservice.com/something-unique>",
  "subscription_public_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
  "subscription_auth": "FPssNDTKnInHVndSTdbKFw=="
}
```

**Response**

Status: `201 Created`

```json
{
  "id": "070af5d3-03a1-4a38-9a75-5b76de8826d2",
  "push_service_url": "<https://some.pushservice.com/something-unique>",
  "subscription_public_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
  "subscription_auth": "FPssNDTKnInHVndSTdbKFw==",
  "created_at": "2022-08-10T17:30:42Z"
}
```
