# Comparing Numeric vs English Representations of Numbers with GPT-4o

Analyzed the accuracy of arithmetic performed on numbers (1-5 digits) vs English representations of the same numbers to see if there is a visible difference. Results show that there is a discrepancy in acuracy for arithmetic in 4 and 5 digit numbers. This suggests improper tokenization/handling of these English representation of numbers resulting in incorrect arithmetic results.

## Accuracy
**1dcDataset200:** 99% \
**2daDataset200:** 99% \
**2dmDataset200:** 99% \
**2dsDataset200:** 100% \
**3daDataset200:** 100% \
**3dsDataset200:** 100% \
**4daDataset200:** 95% \
**4dsDataset200:** 95% \
**5daDataset200:** 95% \
**5ddsDataset200:** 94%
