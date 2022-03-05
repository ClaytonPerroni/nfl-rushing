from enum import Enum

class SortingEnum(str, Enum):
  # total rushing yards
  yds='yds'
  # longest rush
  lng='lng'
  # total rushing touch downs
  td='td'

class SortingDirectionEnum(str, Enum):
  # ascending
  asc='asc'
  # descending
  desc='desc'

