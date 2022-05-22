#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "702c40be-0f54-4b5e-94a1-c25c4f96de77")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "password123")
