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

**NOTE:**
 - Error out if `title` and `description` are already present in the DB. `400 Bad Request` 
    ```
    {
        "non_field_errors": [
            "The fields title, description must make a unique set."
        ]
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

## Send push notifications to all subscribers

**Endpoint**

```
POST /api/notifications/:id/send
```

**Response**

Status: `200 OK`

```json
{
	"success": true
}
```

**NOTE**
 - Backend triggers webpush requests for all subscribers in the background, and return success to FE.
 - Then it depends on the subscriber's push service to send push messages to their browser.

# Subscriptions

## Create a subscription

**Parameters**


| Field            | Type       | Required | Description                                                                    |
|------------------|------------|----------|--------------------------------------------------------------------------------|
| id               | UUID       | yes      | (response only attribute) UUID of the Subscription object                      |
| push_service_url | char (200) | yes      | Push Service Endpoint to make web push protocol requests                       |
| public_key       | char (200) | yes      | public "p256dh" client key from the subscription data                          |
| auth_key         | char (100) | yes      | private "auth" client key from the subscription data                           |
| created_at       | datetime   | yes      | (response only attribute) Timestamp of when the Subscription object is created |
|                  |            |          |                                                                                |


**Endpoint**

```
POST /api/subscriptions
```

**Request**

```json
{
  "push_service_url": "<https://some.pushservice.com/something-unique>",
  "public_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
  "auth_key": "FPssNDTKnInHVndSTdbKFw=="
}
```

**Response**

Status: `201 Created`

```json
{
  "id": "070af5d3-03a1-4a38-9a75-5b76de8826d2",
  "push_service_url": "<https://some.pushservice.com/something-unique>",
  "public_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
  "auth_key": "FPssNDTKnInHVndSTdbKFw==",
  "created_at": "2022-08-10T17:30:42Z"
}
```
