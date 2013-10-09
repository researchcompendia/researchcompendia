import datetime
import hashlib


def upload_path(pathsegment, filename):
    """ Constructs an upload path for a filename """

    bucket_datetime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return "/{segment}/{timehash}-{datetime}/{filename}".format(
        segment=pathsegment,
        # introduce a little randomness in the bucket name
        # http://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html
        timehash=hashlib.md5(bucket_datetime).hexdigest(),
        datetime=bucket_datetime,
        filename=filename,
    )
