(** Coq test file *)

Definition plus1 x := x + 1.

Lemma  plus1_lt:
    forall x,
        x < plus1 x.
Proof. lia. Qed.

Record position: Type := create_position {
  x: nat;
  y: nat;
}.

Theorem plus1_twice:
    forall x,
        plus1 (plus1 x) = x + 2.
Proof. lia. Qed.

Theorem plus1_twice:
    forall x,
        plus1 (plus1 x) = x + 2.
Proof. lia. Qed.
