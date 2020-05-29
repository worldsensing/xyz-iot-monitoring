# -*- coding: utf-8 -*-
import datetime


def translate_datetime(m_datetime):
    return m_datetime.replace(tzinfo=datetime.timezone.utc).isoformat()
