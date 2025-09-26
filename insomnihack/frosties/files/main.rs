use frost_core::compute_lagrange_coefficient;
use frost_secp256k1::{
    self, 
    Identifier, 
    SigningKey, 
    rand_core::OsRng, 
    round2::SignatureShare
};

use std::collections::BTreeSet;

fn str_to_scalar(s: &str) -> k256::Scalar {
    SignatureShare::deserialize(&hex::decode(s).unwrap())
        .unwrap()
        .share()
        .0
}

fn main() {
    let ids: Vec<Identifier> = (1..=3)
        .map(|i| Identifier::new(k256::Scalar::from(i as u64)).unwrap())
        .collect();

    let shares = [
        // (from, to, share)
        (0, 1, "..."),
        (0, 2, "..."),
        (1, 0, "..."),
        (1, 2, "..."),
        (2, 0, "..."),
        (2, 1, "..."),
    ]
    .map(|(from, to, share)| (from, to, str_to_scalar(share)));

    let mut secret = k256::Scalar::ZERO;

    for participant in 0..3 {
        // sent for current participant
        let participant_shares: Vec<_> = shares
            .iter()
            .filter(|(from, _, _)| *from == participant)
            .map(|(_, to, share)| (ids[*to].clone(), *share))
            .collect();

        let points: BTreeSet<_> = participant_shares
            .iter()
            .map(|(id, _)| id.clone())
            .collect();

        // interpolate for f_i(0)
        let mut participant_secret = k256::Scalar::ZERO;
        for (id, share) in participant_shares {
            let lagrange = 
                compute_lagrange_coefficient(&points, None, id).unwrap();
            participant_secret += lagrange * share;
        }

        secret += participant_secret;
    }

    let key = SigningKey::from_scalar(secret).unwrap();
    let signed = key.sign(&mut OsRng, b"Give me the flag");
    println!("{}", hex::encode(signed.serialize().unwrap()));
}
