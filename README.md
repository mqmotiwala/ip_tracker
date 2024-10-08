# IP Tracker

Simple Python script to track changes in your router's public IP address.
A notification is sent via Pushover when the IP address changes.

`https://ipv4.icanhazip.com` is used to refresh the router's public IP address.

## Features

- Fetches your current public IPv4 address.
- Compares the current IP address with the previously recorded one.
- Sends notifications using Pushover if the IP address changes.

## Configuration

Create a `.env` file in the root directory of the project with the following environment variables:

   ```env
   PUSHOVER_USER=your_pushover_user_key
   PUSHOVER_APP_TOKEN=your_pushover_app_token
   PUSHOVER_LOG_TOKEN=your_pushover_log_token # optional, can use same as app token if you prefer
   ```