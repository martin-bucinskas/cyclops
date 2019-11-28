# CyclOps

CyclOps is a CLI for managing AWS Lambdas.

With CyclOps you can invoke and delete lambda functions straight from your command line without you having to remember complicated scripts or use the AWS website.

## Usage

You can run this tool with Python 3.7.

```Shell
pip install
python main.py --profile <YOUR_AWS_PROFILE>
```

Replace the `<YOUR_AWS_PROFILE>` with any profile that has been provided in your aws `credentials` file.
You can usually find your `credentials` file here `~/.aws/credentials`.

## CI, CD and Coverage

You can find the code coverage at the [codecov.io](https://codecov.io/github/martin-bucinskas/cyclops).
If the code coverage drops, the build should fail immediately.